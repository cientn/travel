from backend.database import Connect
import sys


def login(id):
    conn = None
    sql = """SELECT * FROM account WHERE username=%s AND password=%s"""
    values = (id.getUsername(), id.getPassword())
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql, values)
        result = cusor.fetchone()
        cusor.close()
        conn.close()

    except:
        print('Error', sys.exc_info())

    finally:
        del values, sql, conn
        return result


def signup_account(acc):
    # conn = None
    sql = """INSERT INTO account (username, password) VALUES (%s, %s)"""
    values = (acc.getUsername(), acc.getPassword())
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql, values)
        conn.commit()
        result = cusor.rowcount
        cusor.close()
        conn.close()

    except:
        print('Error', sys.exc_info())

    finally:
        del values, sql, conn
        return result


def airport() -> list:
    global list_airport
    sql = """SELECT nameairport, iata FROM airport"""
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchall()
        list_airport = []
        # save
        for row in result:
            ele = row[0] + ' ({})'.format(row[1])
            list_airport.append(ele)

        cusor.close()
        conn.close()
    except:
        print('Error', sys.exc_info())
    finally:
        del sql, conn, result
        return list_airport


def add_ticket(ticket):
    sql = """INSERT INTO ticket(no, class, num_flight, carrier, gate, passenger, departure, arrival, day1, day2, seat, baggage, time_flight, open_gate) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        ticket.getNo(),
        ticket.getClas(),
        ticket.getNumFlight(),
        ticket.getCarrier(),
        ticket.getGate(),
        ticket.getPassenger(),
        ticket.getDeparture(),
        ticket.getArrival(),
        ticket.getDay1(),
        ticket.getDay2(),
        ticket.getSeat(),
        ticket.getBaggage(),
        ticket.getTimeFlight(),
        ticket.getOpenGate()
    )
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql, values)
        conn.commit()
        result = cusor.rowcount
        cusor.close()
        conn.close()

    except:
        print('Error', sys.exc_info())

    finally:
        del values, sql, conn
        return result


def retrieve_ticket():
    global list_ticket
    sql = """SELECT * FROM ticket"""
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchall()
        list_ticket = []
        # save
        for row in result:
            list_ticket.append(row)

        cusor.close()
        conn.close()
    except:
        print('Error', sys.exc_info())
    finally:
        del sql, conn, result
        return list_ticket


def searching(condition):
    global list_result
    sql = f"SELECT * FROM ticket WHERE {condition} '1'"

    list_result = []
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        # print(condition)
        cusor.execute(sql)
        result = cusor.fetchall()
        # print(result)
        # save
        for row in result:
            list_result.append(row)

        cusor.close()
        conn.close()
    except:
        print('Error', sys.exc_info())
    finally:
        del sql, conn, result
        return list_result


def row_collect(stt):
    sql = f"SELECT * FROM ticket WHERE stt='{stt}'"
    result = None
    try:
        conn = Connect()
        cusor = conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchone()
    except:
        print('Error', sys.exc_info())
    finally:
        del sql, conn
        return result
