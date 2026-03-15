import os
import sys
from scraper import WebScraper
from generator import ContentGenerator
from trainer import ModelTrainer

class Bot:
    def __init__(self):
        self.scraper = WebScraper()
        self.generator = ContentGenerator()
        self.trainer = ModelTrainer()
        self.data_folder = "datos_entrenamiento"
        
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def descargar_contenido(self, url):
        """Descarga contenido de un sitio web"""
        print(f"Descargando contenido de {url}...")
        contenido = self.scraper.descargar(url)
        
        if contenido:
            # Guardar contenido
            archivo = os.path.join(self.data_folder, "contenido_descargado.txt")
            with open(archivo, 'a', encoding='utf-8') as f:
                f.write(contenido + "\n")
            print(f"✓ Contenido guardado en {archivo}")
            return True
        else:
            print("✗ No se pudo descargar contenido")
            return False
    
    def entrenar(self):
        """Entrena el modelo con los datos descargados"""
        print("Entrenando el modelo...")
        archivo = os.path.join(self.data_folder, "contenido_descargado.txt")
        
        if os.path.exists(archivo):
            self.trainer.entrenar(archivo)
            print("✓ Modelo entrenado exitosamente")
        else:
            print("✗ No hay datos para entrenar. Descarga contenido primero.")
    
    def generar(self, cantidad=5, semilla=None):
        """Genera nuevo contenido"""
        print(f"Generando {cantidad} fragmentos de contenido...")
        contenido_generado = self.generator.generar(cantidad, semilla)
        return contenido_generado
    
    def mostrar_menu(self):
        """Muestra el menú interactivo"""
        while True:
            print("\n" + "="*50)
            print("BOT GENERADOR DE CONTENIDO")
            print("="*50)
            print("1. Descargar contenido de una web")
            print("2. Entrenar el modelo")
            print("3. Generar contenido")
            print("4. Ver contenido guardado")
            print("5. Salir")
            print("="*50)
            
            opcion = input("Elige una opción (1-5): ").strip()
            
            if opcion == "1":
                url = input("Ingresa la URL del sitio web: ").strip()
                self.descargar_contenido(url)
            
            elif opcion == "2":
                self.entrenar()
            
            elif opcion == "3":
                try:
                    cantidad = int(input("¿Cuántos fragmentos quieres generar? (default 5): ") or "5")
                    contenido = self.generar(cantidad)
                    print("\n--- CONTENIDO GENERADO ---")
                    for i, texto in enumerate(contenido, 1):
                        print(f"\n{i}. {texto}")
                except ValueError:
                    print("✗ Ingresa un número válido")
            
            elif opcion == "4":
                archivo = os.path.join(self.data_folder, "contenido_descargado.txt")
                if os.path.exists(archivo):
                    with open(archivo, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                    print("\n--- CONTENIDO GUARDADO ---")
                    print(contenido[:500] + "..." if len(contenido) > 500 else contenido)
                else:
                    print("✗ No hay contenido guardado")
            
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            
            else:
                print("✗ Opción no válida")

if __name__ == "__main__":
    bot = Bot()
    bot.mostrar_menu()