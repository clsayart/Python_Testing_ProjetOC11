from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def show_summary(self):
        self.client.post('/showSummary', data={'email': 'kate@shelifts.co.uk'})

    @task
    def book(self):
        self.client.get('/book/Spring Festival/She Lifts')

    @task
    def purchase_places(self):
        self.client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                  'places': '6'})

    @task
    def display_points(self):
        self.client.get('/displayPoints')

    @task
    def logout(self):
        self.client.get('/logout')
