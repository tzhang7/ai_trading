""" A Simple Order Routing Mechanism """

from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection, message
def error_handler(msg):

    print("Server Error:", msg)

def server_handler(msg):

    print("Server Msg:", msg.typeName, "-", msg)

def acct_update(msg):
    print(msg)

def create_contract(symbol, sec_type, exch, prim_exch, curr):
    contract = Contract()
    contract.m_symbol = symbol
    contract.m_secType = sec_type
    contract.m_exchange = exch
    contract.m_primaryExch = prim_exch
    contract.m_currency = curr
    return contract

def create_order(order_type, quantity, action):
    order = Order()
    order.m_orderType = order_type
    order.m_totalQuantity = quantity
    order.m_action = action
    return order

if __name__ == "__main__":

    client_id = 999
    order_id = 123
    port = 7497

    tws_conn = None

    try:
        # Establish connection to TWS.
        tws_conn = Connection.create(port=port,clientId=client_id)

        tws_conn.connect()
        # Assign error handling function.
        tws_conn.register(error_handler, 'Error')
        tws_conn.register(acct_update,
                     message.updateAccountValue,
                     message.updateAccountTime,
                     message.updatePortfolio)
        # Assign server messages handling function.
        tws_conn.registerAll(server_handler)
        # Create AAPL contract and send order
        tvix_contract = create_contract('TVIX',
        'STK',
        'SMART',
        'SMART',
        'USD')

        # Request account info
        tws_conn.reqAccountUpdates(True,'DU1670873')
        # Go long 100 shares of AAPL

        #tvix_order = create_order('MKT', 100, 'SELL')

        # Place order on IB TWS.

        #tws_conn.placeOrder(order_id, tvix_contract, tvix_order)
    finally:
    # Disconnect from TWS

        if tws_conn is not None:

            tws_conn.disconnect()