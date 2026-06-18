class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {}

        for i, restaurant in enumerate(list1):
            pos[restaurant] = i

        result = []
        min_sum = float('inf')

        for j, restaurant in enumerate(list2):
            if restaurant in pos:
                index_sum = pos[restaurant] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]

                elif index_sum == min_sum:
                    result.append(restaurant)

        return result