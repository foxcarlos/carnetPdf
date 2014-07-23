from fpdf import FPDF
import dbf

class CrearNxxmast:
    def __init__(self):
        ''' '''
        
    def dbf2List(self, tabla, parametros):
        useTabla = dbf.Table(tabla)
        useTabla.open()
        consulta = 'select * where status == "1"'
        busqueda = useTabla.query('select * where status == "1"')
        #(reg[1], reg[2], reg[4], reg[40], reg[58])
        #lista = [reg for reg in busqueda]  # useTabla]
        lista = [reg for reg in useTabla]
        return lista
    
    def tablaNxxmast(self):
        nxxMast = []
        rutaArchivoDbf = '/media/serv_coromoto/Nomina/asencwin/nominaw/ncsmast.dbf'
        rutaArchivoDbf2 = '/media/serv_coromoto/Nomina/asencwin/nominaw/ncmmast.dbf'
        rutaArchivoDbf3 = '/media/serv_coromoto/Nomina/asencwin/nominaw/nepmast.dbf'
        rutaArchivoDbf4 = '/media/serv_coromoto/Nomina/asencwin/nominaw/nmdmast.dbf'
        rutaArchivoDbf5 = '/media/serv_coromoto/Nomina/asencwin/nominaw/nnmmast.dbf'
    
        cs = self.dbf2List(rutaArchivoDbf)
        nxxMast.extend(cs)
    
        cm = self.dbf2List(rutaArchivoDbf2)
        nxxMast.extend(cm)
    
        ep = self.dbf2List(rutaArchivoDbf3)
        nxxMast.extend(ep)
    
        md = self.dbf2List(rutaArchivoDbf4)
        nxxMast.extend(md)
    
        nm = self.dbf2List(rutaArchivoDbf5)
        nxxMast.extend(nm)        
        return nxxMast
    
class MyPDF(FPDF):
    def buscar(self, cedula):
        self.cedula = cedula
        
    def footer(self):
        apellidos = 'GARCIA DIAZ'
        nombres = 'CARLOS ALBERTO'
        
        #Agrego Nombre del Empleado y lo ubico en el pie de pagina
        self.set_font('Arial', 'B', 10)
        self.set_y(-10)      
        self.cell(0, 7, apellidos, align="C")
        self.ln(2)
        self.cell(0, 11, nombres, align="C") 

    def header(self):
        imgBandera = "Bandera.JPG"
        imgFondo = "FONDOCARNET.jpg"
        imgLogo = "HOSPITALC.JPG"
        imgFoto = '/media/serv_coromoto/NominaShc/FotosE/F0011951.jpg'
        
        #Agrego las Imagenes de cabecera
        self.image(imgFondo, 0,11,w=55,h=81)
        self.image(imgBandera,0,10,w=55,h=11)
        
class ReportTablePDF:

    def __init__(self):
        self.pdf = MyPDF(orientation='P',unit='mm',format=(55,85))

    def imprimir(self):  
        cabe1 = 'REPUBLICA BOLIVARIANA DE VENEZUELA'
        cabe2 = 'PDV SERVICIOS DE SALUD S.A.'
        cabe3 = 'HOSPITAL'
        cabe4 = 'COROMOTO'
        
        self.pdf.add_page()
        self.pdf.ln(13)

        #Primer Texto y tipo de letra
        self.pdf.set_font('Arial', 'B', 7)
        self.pdf.set_text_color(255,0,0)
        self.pdf.cell(w=0,h=0,txt=cabe1,border=0,ln=1,align='C')
        
        #Segundo Texto y tipo de letra
        self.pdf.set_font('Arial', 'B', 9)
        self.pdf.set_text_color(255,0,0)
        self.pdf.cell(w=0,h=7,txt=cabe2,border=0,ln=1,align='C')
        
        #Imagen del Logo
        self.pdf.image(imgLogo,5, 29, w=9, h=12)
        
        #Tercer Texto y tipo de letra
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0,4, cabe3, 0, 1, 'C')
        self.pdf.cell(0,8, cabe4, 0, 1, 'C')
        
        #Imagen de la Foto
        self.pdf.image(imgFoto,15,42,w=25,h=33)
        self.pdf.output('PRUEBA.PDF','F')  

#pdf = ReportTablePDF()
#pdf.imprimir()
nx = CrearNxxmast()
reg = nx.tablaNxxmast()
ficha = reg[1][1]
nombre = reg[1][2]
tipov = reg[1][3]
cedula = reg[1][4]
for f in reg:
    if 9743147 in f:
        print('si')
    
#print(reg[1][1])
