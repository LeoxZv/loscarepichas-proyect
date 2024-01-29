#tenemos un trabajor que gana 69.230 AL DIA durante 26 dia laborales,
# nos pien hallar cuanto recibe un sueldo y cuanto se aporta a su seguro de pension si se sabe que el porcentaje de aporte mensual es el 11.74% el cual esta compuesto por
#10% ingresa a su AFP
# 0.38% COBRO DE ADMIN E INVERSION DE TU FONDO
#1.36% POR SEGURO DE INVALIDZ,SOOBREV, GASTOS DE SEPELIO

dia_trabajador = 69230
dias_trabajados = 26

sueldo = dia_trabajador*dias_trabajados
print("Su sueldo es de:",sueldo)

porcentaje_s = sueldo * 0.1174
print("El porcentaje total del sueldo es:",porcentaje_s)

porcentaje_AFP = sueldo * 0.1
print("El porcentaje de AFP es de:",porcentaje_AFP)

porcentaje_caif = sueldo * 0.0038
print("El porcentaje de cobro por administracion:",porcentaje_caif)

porcentaje_seguro = sueldo * 0.0136
print("El porcentaje seguro:",porcentaje_seguro)







