class Ticket:
    def __init__(self, no, clas, num_flight, carrier, gate, passenger, departure, arrival, day1, day2, seat, baggage,
                 time_flight, open_gate):
        self.no = no
        self.clas = clas
        self.num_flight = num_flight
        self.carrier = carrier
        self.gate = gate
        self.passenger = passenger
        self.departure = departure
        self.arrival = arrival
        self.day1 = day1
        self.day2 = day2
        self.seat = seat
        self.baggage = baggage
        self.time_flight = time_flight
        self.open_gate = open_gate

    # dinh nghia get va set
    def getNo(self):
        return self.no

    def getClas(self):
        return self.clas

    def getNumFlight(self):
        return self.num_flight

    def getCarrier(self):
        return self.carrier

    def getGate(self):
        return self.gate

    def getPassenger(self):
        return self.passenger

    def getDeparture(self):
        return self.departure

    def getArrival(self):
        return self.arrival

    def getDay1(self):
        return self.day1

    def getDay2(self):
        return self.day2

    def getSeat(self):
        return self.seat

    def getBaggage(self):
        return self.baggage

    def getTimeFlight(self):
        return self.time_flight

    def getOpenGate(self):
        return self.open_gate

    def setNo(self, no):
        self.no = no

    def setClas(self, clas):
        self.clas = clas

    def setNumFlight(self, num_flight):
        self.num_flight = num_flight

    def setCarrier(self, carrier):
        self.carrier = carrier

    def setGate(self, gate):
        self.gate = gate

    def setPassenger(self, passenger):
        self.passenger = passenger

    def setDeparture(self, departure):
        self.departure = departure

    def setArrival(self, arrival):
        self.arrival = arrival

    def setDay1(self, day1):
        self.day1 = day1

    def setDay2(self, day2):
        self.day2 = day2

    def setSeat(self, seat):
        self.seat = seat

    def setBaggage(self, baggage):
        self.baggage = baggage

    def setTimeFlight(self, time_flight):
        self.time_flight = time_flight

    def setOpenGate(self, open_gate):
        self.open_gate = open_gate

    def __str__(self):
        str_sql = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
            self.no,
            self.clas,
            self.num_flight,
            self.carrier,
            self.gate,
            self.passenger,
            self.departure,
            self.arrival,
            self.day1,
            self.day2,
            self.seat,
            self.baggage,
            self.time_flight,
            self.open_gate
        )

        return str_sql
