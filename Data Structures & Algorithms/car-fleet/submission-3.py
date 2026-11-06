class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p,s in zip(position,speed): pair.append([p,s])
        carStack = []

        for p,s in sorted(pair)[::-1]:
            time = (target - p) / s
            carStack.append(time)

            if len(carStack) > 1 and carStack[-1] <= carStack[-2]:
                carStack.pop()
        return len(carStack)