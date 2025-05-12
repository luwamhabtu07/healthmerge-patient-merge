# Patient Record Merge - HealthMerge Inc. & CarePlus Integration

## 🩺 Problem Statement

HealthMerge Inc. has acquired CarePlus, and both companies maintain separate digital patient records sorted by SSN (Social Security Number). Your task is to merge these two sorted linked lists into one, maintaining sorted order and preserving all patient records.

---

## 🧠 Clarifying Questions

1. Can duplicate SSNs appear in both lists?  
   → Yes, we keep both since patient data may differ.
2. Are the input lists guaranteed to be sorted by SSN?  
   → Yes.
3. Can any of the lists be empty?  
   → Yes.

---

## 🔄 Solution Overview

We iterate over both lists and compare SSN values node by node, appending the smaller node to the result list. If either list runs out, we attach the rest of the other list.

---

## 🧪 Test Cases

### ✅ Normal Cases
- Merging two non-empty sorted lists.
- Lists with overlapping SSNs.
- One list is a subset of the other.

### ⚠️ Edge Cases
- One or both input lists are empty.
- Nodes with the same SSN but different patient data.
- Very large lists to test performance.

---

## 📈 Time & Space Complexity

- **Time Complexity**: `O(n + m)` where `n` and `m` are the lengths of the two lists.
- **Space Complexity**: `O(1)` extra space (excluding output list nodes; we reuse existing nodes).

---

## 🧪 How to Run Tests

Make sure you're in the project root directory, then run:

```bash
python3 -m unittest tests/test_merge_records.py
