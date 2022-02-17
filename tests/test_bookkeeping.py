import unittest
from unittest.mock import patch
import bookkeeping


class TestFunctions(unittest.TestCase):
    def test_show_document_info(self):
        test_case = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        expected_result = [
            'passport "2207 876234" "Василий Гупкин"',
            'invoice "11-2" "Геннадий Покемонов"',
            'insurance "10006" "Аристарх Павлов"'
        ]
        result = [bookkeeping.show_document_info(i) for i in test_case]
        self.assertListEqual(result, expected_result)

    @patch.object(bookkeeping, 'append_doc_to_shelf')
    def test_add_new_doc(self, mock_append_doc_to_shelf):
        mock_append_doc_to_shelf.return_value = True
        result = bookkeeping.add_new_doc()
        self.assertEqual('3', result)

    @patch.object(bookkeeping, 'remove_doc_from_shelf')
    def test_delete_doc(self, mock_remove_doc_from_shelf):
        mock_remove_doc_from_shelf.return_value = True
        result = bookkeeping.delete_doc()
        self.assertEqual(('11-2', True), result)
