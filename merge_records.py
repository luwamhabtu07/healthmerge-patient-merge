from src.patient_record import PatientRecord


def merge_sorted_records(head1, head2):
    dummy = PatientRecord(0, '', 0)
    tail = dummy

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2
    return dummy.next
