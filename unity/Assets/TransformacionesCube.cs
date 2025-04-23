using UnityEngine;

public class TransformacionesObjeto : MonoBehaviour
{
    public float intervaloMovimiento = 2f;
    private float tiempoAcumulado = 0f;

    void Update()
    {
        tiempoAcumulado += Time.deltaTime;

        if (tiempoAcumulado >= intervaloMovimiento)
        {
            tiempoAcumulado = 0f;

            float aleatorioX = Random.Range(-1f, 1f);
            float aleatorioY = Random.Range(-1f, 1f);
            transform.Translate(new Vector3(aleatorioX, aleatorioY, 0));
        }

        float velocidadRotacion = 50f;
        transform.Rotate(Vector3.up, velocidadRotacion * Time.deltaTime);

        float escala = Mathf.Lerp(0.8f, 1.2f, (Mathf.Sin(Time.time) + 1f) / 2f);
        transform.localScale = new Vector3(escala, escala, escala);
    }
}
