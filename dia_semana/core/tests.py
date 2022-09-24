from django.test import TestCase

class DomingoTest(TestCase):
   def setUp(self):
      self.resp = self.client.get('/')

   def test_200_response(self):
      self.assertEqual(200, self.resp.status_code)

   def test_texto(self):
      self.assertContains(self.resp, 'domingo')

def test_template_domingo(self):
    self.assertTemplateUsed(self.resp, 'domingo.html')
