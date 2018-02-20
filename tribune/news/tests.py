from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    # set up method
    
    def setUp(self):
        self.james= Editor(first_name = 'James',last_name= 'Muriuki', email='james@moringaschool.com')
    
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()

        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.james= Editor(first_name = 'James',last_name= 'Muriuki', email='james@moringaschool.com')
        self.james.save_editor()
        self.james.delete_editor()
        editors = Editor.objects.all()
        
        self.assertTrue(len(editors) <1)

    # def test_update_method(self):
    #     self.james = Editor(
    #         first_name='James', last_name='Muriuki', email='james@moringaschool.com')
    #     self.james.save_editor()
    #     self.james.update_editor()
    #     last_name = "Ulemsee"
    #     self.assertTrue(self.james.update_editor(), last_name)
        

        

 
