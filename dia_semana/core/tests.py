from django.test import TestCase
from core.models import Dia_semanaModel
from datetime import datetime

class SemDomingoTest(TestCase):
   def setUp(self):
      self.resp = self.client.get('/')

   def test_200_response(self):
      self.assertEqual(200, self.resp.status_code)

   def test_texto(self):
      self.assertContains(self.resp, 'Lamento')
      self.assertContains(self.resp, 'hoje não é domingo')

def test_template_domingo(self):
    self.assertTemplateUsed(self.resp, 'domingo.html')

class ComDomingoTest(TestCase):
   def setUp(self):
      today = datetime.today()
      dia_calendario = Dia_semanaModel(name = 'Domingo', day = today.day, month = today.month)
      dia_calendario.save()
      self.resp = self.client.get('/')

   def test_bd_fake(self):
      self.assertTrue(Dia_semanaModel.objects.exists())

   def test_200_response(self):
      self.assertEqual(200, self.resp.status_code)

   def test_texto(self):
      self.assertContains(self.resp, 'domingo')

   def test_template_domingo(self):
      self.assertTemplateUsed(self.resp, 'domingo.html')

class DomingoModelTest(TestCase):
    def setUp(self):
        self.dia_semana = 'Sabado'
        self.month      = 12
        self.day        = 25
        self.cadastre   = Dia_semanaModel(
            name  = self.dia_semana,
            day   = self.day,
            month = self.month,
        )
        self.cadastre.save()

    def test_created(self):
        self.assertTrue(Dia_semanaModel.objects.exists())

    def test_modified_in(self):
        self.assertIsInstance(self.cadastre.modified_in, datetime)

    def test_name_dia_semana(self):
        name = self.cadastre.__dict__.get('name', '')
        self.assertEqual(name, self.dia_semana)

    #def test_day(self):
        #day = self.cadastre.__dict__.get('day', '')
        #self.assertEqual(day, self.day)
