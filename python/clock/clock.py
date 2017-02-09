class Clock:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self._normalize()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.hours == self.hours and other.minutes == self.minutes:
            return True
        return False

    def __str__(self):
        return '%02d:%02d' % (self.hours, self.minutes)

    def _normalize(self):
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

    def add(self, minutes):
        self.minutes += minutes
        self._normalize()
        return self
