# Problem: https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: Iterate and merge
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlap
                # Merge the intervals
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add to result
                merged.append(current)

        return merged
