import { useRef } from "react";
import { useFrame } from "@react-three/fiber";

export default function CuboAnimado() {
  const ref = useRef();

  useFrame(({ clock }) => {
    const t = clock.getElapsedTime();
    if (ref.current) {
      ref.current.rotation.y = t;
      ref.current.rotation.x = t / 2;
      ref.current.position.x = Math.sin(t);
      ref.current.position.z = Math.cos(t);
      const escala = 1 + 0.3 * Math.sin(t * 2);
      ref.current.scale.set(escala, escala, escala);
    }
  });

  return (
    <mesh ref={ref}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="orange" />
    </mesh>
  );
}
