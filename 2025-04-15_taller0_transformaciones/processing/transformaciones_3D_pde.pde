void setup() {
  size(800, 600, P3D); // Sketch en 3D
}

void draw() {
  background(220, 245, 255); 
  lights();

  float t = millis() / 1000.0; // Tiempo en segundos

  pushMatrix();

  translate(width/2, height/2, 0);

  float desplazamientoX = sin(t) * 100;
  float desplazamientoY = cos(t) * 100;
  translate(desplazamientoX, desplazamientoY, 0);

  float escala = 1 + 0.3 * sin(t * 2);
  scale(escala);

  rotateX(t);
  rotateY(t * 1.2);


  fill(255, 105, 180); 
  box(100);

  popMatrix();
}
