from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''testing new user created or not '''
        email = 'test@mech2it.com'
        password = 'shree123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email email validation(normalize_email)'''
        email = 'test@MEch2IT.COM'
        user = get_user_model().objects.create_user(email, 'shree123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_null_email(self):
        '''test eamil is not null or just a string'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'shree123')

    def test_create_new_superuser(self):
        '''create super user '''
        user = get_user_model().objects.create_superuser(
            'test@mech2it.com',
            'shree123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
