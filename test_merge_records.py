import unittest
from src.patient_record import PatientRecord
from src.merge_records import merge_sorted_records

def build_linked_list(data):
    if not data:
        return None
    head = PatientRecord(*data[0])
    current = head
    for record in data[1:]:
        current.next = PatientRecord(*record)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append((head.ssn, head.name, head.age))
        head = head.next
    return result

class TestMergeRecords(unittest.TestCase):

    # Normal Case 1: Two sorted lists with unique SSNs
    def test_merge_normal(self):
        list1 = build_linked_list([(101, "Alice", 29), (105, "Bob", 34)])
        list2 = build_linked_list([(103, "Charlie", 45), (106, "David", 50)])
        merged = merge_sorted_records(list1, list2)
        expected = [(101, "Alice", 29), (103, "Charlie", 45), (105, "Bob", 34), (106, "David", 50)]
        self.assertEqual(linked_list_to_list(merged), expected)

    # Normal Case 2: One list is a subset of the other
    def test_subset_list(self):
        list1 = build_linked_list([(102, "Eva", 40)])
        list2 = build_linked_list([(100, "Frank", 60), (102, "Eva", 40), (104, "Grace", 35)])
        merged = merge_sorted_records(list1, list2)
        expected = [(100, "Frank", 60), (102, "Eva", 40), (102, "Eva", 40), (104, "Grace", 35)]
        self.assertEqual(linked_list_to_list(merged), expected)

    # Normal Case 3: Both lists have multiple entries, no overlap
    def test_no_overlap(self):
        list1 = build_linked_list([(100, "Jack", 20), (102, "Jill", 25)])
        list2 = build_linked_list([(103, "Tom", 30), (104, "Tina", 28)])
        merged = merge_sorted_records(list1, list2)
        expected = [(100, "Jack", 20), (102, "Jill", 25), (103, "Tom", 30), (104, "Tina", 28)]
        self.assertEqual(linked_list_to_list(merged), expected)

    # Edge Case 1: One list is empty
    def test_one_empty_list(self):
        list1 = None
        list2 = build_linked_list([(101, "Solo", 31)])
        merged = merge_sorted_records(list1, list2)
        expected = [(101, "Solo", 31)]
        self.assertEqual(linked_list_to_list(merged), expected)

    # Edge Case 2: Both lists are empty
    def test_both_empty_lists(self):
        merged = merge_sorted_records(None, None)
        self.assertIsNone(merged)

    # Edge Case 3: Duplicate SSNs with different data
    def test_duplicate_ssn(self):
        list1 = build_linked_list([(101, "Ana", 25)])
        list2 = build_linked_list([(101, "Anna", 30)])
        merged = merge_sorted_records(list1, list2)
        expected = [(101, "Ana", 25), (101, "Anna", 30)]
        self.assertEqual(linked_list_to_list(merged), expected)

if __name__ == '__main__':
    unittest.main()

