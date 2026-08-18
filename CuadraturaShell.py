import sys

# Almacena el dinero depositado por trabajador
db_trabajadores = {}

def pedir_entero(mensaje):
    """Pide un número. Enter/Espacio = 0. Letras = error."""
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return 0
        try:
            return int(entrada)
        except ValueError:
            print("Error: Por favor, ingrese solo números. Inténtelo de nuevo.\n")

def pedir_confirmacion(mensaje):
    """Pide confirmación (sí/no)."""
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in ['1', 'si', 'sí', 's']:
            return True
        elif entrada in ['2', 'no', 'n']:
            return False
        else:
            print("Error: Por favor, ingrese 'si' (1) o 'no' (2).\n")

def pedir_datos_trabajador():
    """Solicita nombre y turno."""
    nombre = input("\nIngrese su nombre: ").strip().title()
    
    while True:
        turno_input = input("Ingrese su turno (1: Día, 2: Tarde, 3: Noche): ").strip().lower()
        if turno_input in ['1', 'dia', 'día']:
            turno = 'Día'
            break
        elif turno_input in ['2', 'tarde']:
            turno = 'Tarde'
            break
        elif turno_input in ['3', 'noche']:
            turno = 'Noche'
            break
        else:
            print("Turno no válido. Ingrese 1, 2, 3, o escriba Dia, Tarde o Noche.\n")
            
    return nombre, turno

def realizar_deposito(nombre):
    """Gestiona el conteo de billetes y depósito."""
    denominaciones = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 10]
    
    while True:
        print(f"\n--- CONTANDO BILLETES DE {nombre.upper()} ---")
        print("(Presione ENTER si no tiene billetes de ese valor)")
        suma_temporal = 0
        
        for billete in denominaciones:
            cantidad = pedir_entero(f"Cantidad de billetes/monedas de ${billete}: ")
            subtotal = cantidad * billete
            suma_temporal += subtotal
        
        print("\n" + "="*40)
        print(f"Monto total depositado por {nombre}: ${suma_temporal:,}")
        print("="*40)
        
        seguro = pedir_confirmacion("¿Está seguro de su depósito? (1: Sí / 2: No): ")
        
        if seguro:
            # Registra nuevo trabajador si no existe
            if nombre not in db_trabajadores:
                db_trabajadores[nombre] = 0
            
            # Suma al total acumulado
            db_trabajadores[nombre] += suma_temporal
            print(f"Depósito guardado exitosamente. Total acumulado en caja: ${db_trabajadores[nombre]:,}\n")
            break
        else:
            print("\nDepósito cancelado. Empecemos a contar desde cero...")
            # Reinicia el ciclo para volver a contar

def realizar_cuadratura(nombre):
    """Gestiona el cálculo de la cuadratura."""
    print(f"\n--- CUADRATURA DE {nombre.upper()} ---")
    
    if nombre not in db_trabajadores or db_trabajadores[nombre] == 0:
        print("Atención: No hay dinero depositado a su nombre. Su depósito se tomará como $0.")
        deposito_actual = 0
    else:
        deposito_actual = db_trabajadores[nombre]
        print(f"Dinero depositado: ${deposito_actual:,}")
        
    while True:
        print("\nIngrese los siguientes montos (Presione ENTER si es 0):")
        ventas_totales = pedir_entero("1. Turno Completo (Ventas Totales): $")
        transbank = pedir_entero("2. Transbank (Monto total máquina): $")
        shellcard = pedir_entero("3. Shellcard: $")
        aplicacion = pedir_entero("4. Aplicación (MiCopiloto/AppShell): $")
        transferencia = pedir_entero("5. Transferencias: $")
        
        total_ingresos = deposito_actual + transbank + shellcard + aplicacion + transferencia
        diferencia = total_ingresos - ventas_totales
        
        print("\n" + "="*40)
        print("RESUMEN DE CUADRATURA")
        print(f"Ventas Esperadas:   ${ventas_totales:,}")
        print(f"Total Ingresado:    ${total_ingresos:,} (Incluye Depósito y Tarjetas)")
        
        if diferencia > 0:
            print(f"Diferencia:      +${diferencia:,} (SOBRA DINERO)")
        elif diferencia < 0:
            print(f"Diferencia:       ${diferencia:,} (FALTA DINERO)")
        else:
            print(f"Diferencia:       ${diferencia:,} (CUADRADO PERFECTAMENTE)")
        print("="*40)
        
        print("\nOpciones de Cuadratura:")
        print("1. Aceptar Cuadratura")
        print("2. Modificar Cuadratura (Empezar de nuevo)")
        print("3. Salir sin guardar")
        
        while True:
            opcion_cuad = input("Seleccione una opción: ").strip().lower()
            if opcion_cuad in ['1', 'aceptar']:
                print("\n¡CUADRATURA ACEPTADA!")
                print("Volviendo al menú principal...\n")
                return 
            elif opcion_cuad in ['2', 'modificar']:
                print("\nReiniciando cuadratura... (Su depósito se mantiene intacto)")
                break 
            elif opcion_cuad in ['3', 'salir']:
                print("\nSaliendo de la cuadratura...\n")
                return 
            else:
                print("Opción no válida. Ingrese 1, 2 o 3.")

# --- MENÚ PRINCIPAL ---
def main():
    print("BIENVENIDO AL SISTEMA DE CAJA SHELL")
    
    while True:
        print("-" * 30)
        print("MENÚ PRINCIPAL")
        print("1. Depositar dinero")
        print("2. Hacer cuadratura")
        print("3. Salir")
        print("-" * 30)
        
        opcion = input("Elija una opción (1, 2 o 3): ").strip().lower()
        
        if opcion == '3' or opcion == 'salir':
            print("Cerrando el sistema... ¡Buen turno!")
            sys.exit()
            
        elif opcion == '1' or opcion == 'depositar':
            nombre, turno = pedir_datos_trabajador()
            realizar_deposito(nombre)
            
            # Opciones post-depósito
            while True:
                print("\n¿Qué desea hacer ahora?")
                print("1. Realizar otro depósito (Sumar más dinero)")
                print("2. Hacer la cuadratura")
                print("3. Volver al menú principal")
                
                post_deposito = input("Elija una opción: ").strip()
                if post_deposito == '1':
                    realizar_deposito(nombre)
                elif post_deposito == '2':
                    realizar_cuadratura(nombre)
                    break
                elif post_deposito == '3':
                    break
                else:
                    print("Opción no válida.")
                    
        elif opcion == '2' or opcion == 'cuadratura':
            nombre, turno = pedir_datos_trabajador()
            realizar_cuadratura(nombre)
            
        else:
            print("Opción no reconocida. Por favor, intente de nuevo.\n")

# Inicia el programa
if __name__ == "__main__":
    main()