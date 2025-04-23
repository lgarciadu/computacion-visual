import { Canvas } from "@react-three/fiber";
import CuboAnimado from "./CuboAnimado";
import { Color } from "three";

export default function App() {
  return (
    <Canvas
      camera={{ position: [3, 3, 3], fov: 75 }}
      style={{ width: "100vw", height: "100vh" }}
    >
      {/* Fondo azul claro */}
      <color attach="background" args={["lightblue"]} />

      {/* Iluminación */}
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} />

      {/* Cubo animado */}
      <CuboAnimado />
    </Canvas>
  );
}
