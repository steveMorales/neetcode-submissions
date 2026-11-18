class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Map:
            self.Map[key] = []
        self.Map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Map:
            return ""
        
        entries = self.Map[key]
        left, right = 0, len(entries) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            
            entry_val,entry_time = entries[mid]
            if entry_time == timestamp:
                return entry_val
            elif entry_time < timestamp:
                result = entry_val
                left = mid + 1
            else:
                right = mid - 1
        return result
        
