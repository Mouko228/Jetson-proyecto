import cv2
import time

print("[INFO] Inicializando canal de hardware con la camara...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] No se pudo establecer conexion con /dev/video0.")
    print("[CONSEJO] Verifica el cable de la camara o los permisos de usuario.")
    exit(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("[INFO] Canal establecido. Iniciando prueba de estres por 10 segundos...")

frame_count = 0   
duration = 10.0
start_time = time.time()

while (time.time() - start_time) < duration:
    ret, frame = cap.read()
    if not ret:
        print("[ALERTA] Cuadro perdido detectado en el buffer.")
        continue
    
    frame_count += 1

end_time = time.time()
elapsed_time = end_time - start_time

# Calculo de telemetria final
fps = frame_count / elapsed_time

print(f"Tiempo total de ejecucion: {elapsed_time:.2f} segundos")
print(f"Fotogramas totales procesados: {frame_count}")
print(f"Rendimiento de procesamiento: {fps:.2f} FPS")

# Liberacion obligatoria de recursos del sistema
cap.release()
print("[INFO] Recursos liberados de forma segura")