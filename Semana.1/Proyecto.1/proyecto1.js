const personajes = ["Carlos", "Ana", "Luis", "Sofia", "Miguel"];
const lugares = ["Casa", "Escuela", "Parque", "Biblioteca", "Centro Comercial"];
const animales = ["Perro", "Gato", "Pájaro", "Pez", "Tortuga"];
const acciones = ["Corriendo", "Saltando", "Nadando", "Volando", "Caminando"];
const objetos = ["Libro", "Lápiz", "Computadora", "Teléfono", "Bicicleta"];
const afirmaciones = [ "si", "no" ];

function elementoAleatorio(lista) {
    const indice = Math.floor(Math.random() * lista.length);
    return lista[indice];
}

function obtenerArticulo(lugar) {
    if (["Casa", "Escuela", "Biblioteca"].includes(lugar)) {
        return "La";
    }

    return "El";
}

function obtenerAfirmacion(a) {
    if (a === "si") {
        return "sí habia visto algo asi";
    }
    return "no habia visto algo asi en su vida";
}

function generarHistoria() {
    const personaje = elementoAleatorio(personajes);
    const lugar = elementoAleatorio(lugares);
    const animal = elementoAleatorio(animales);
    const accion = elementoAleatorio(acciones);
    const objeto = elementoAleatorio(objetos);
    const afirmacion = elementoAleatorio(afirmaciones);

    const articulo = obtenerArticulo(lugar);
    const afirmacionTexto = obtenerAfirmacion(afirmacion);
  

    console.log(
        `Una vez un guerrero llamado ${personaje} estaba en ${articulo} ${lugar} cuando vio a un ${animal} que estaba ${accion} con un ${objeto}.
        ${personaje} ${afirmacionTexto}.`
    );



}

generarHistoria();