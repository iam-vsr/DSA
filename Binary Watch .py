class Solution1:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for h in range(12):         # hours: 0 to 11
            for m in range(60):     # minutes: 0 to 59
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append(f"{h}:{m:02d}")  # format minute with leading zero
        return result

#general LED
class Solution2:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def backtrack(leds, start, turnedOn, hour, minute):
            if hour > 11 or minute > 59:
                return
            if turnedOn == 0:
                res.append(f"{hour}:{minute:02d}")
                return
            for i in range(start, len(leds)):
                val, is_hour = leds[i]
                if is_hour:
                    backtrack(leds, i + 1, turnedOn - 1, hour + val, minute)
                else:
                    backtrack(leds, i + 1, turnedOn - 1, hour, minute + val)
        
        res = []
        # LED values and their types (True = hour, False = minute)
        leds = [(1, True), (2, True), (4, True), (8, True),
                (1, False), (2, False), (4, False), (8, False), (16, False), (32, False)]
        
        backtrack(leds, 0, turnedOn, 0, 0)
        return res
