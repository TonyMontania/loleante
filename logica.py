import beconnect


def gestionarProv (nombreprod):
    beconnect.Mostrar("SELECT nombreprod FROM producto WHERE nombreprod = "+ nombreprod )
    pass
def controlarProd(productoid):
    beconnect.Mostrar("SELECT productoid FROM producto WHERE prodcutoid ="+ productoid)
    pass
def comprarProd():
    pass
def controlarStockProd():
    pass
def venderCliente():
    pass
def reservarProd():
    pass

def gestionarProv ():
    Nombre = input ( "xd \t" )
    Descripcion= input ("xd \t")
    sql = "INSERT INTO producto (nombreprod,descripprod) VALUES (%s,%s)" 
    val= [(Nombre,Descripcion)]
    beconnect.EjecutarSQL_VAL(sql, val)

gestionarProv ()
