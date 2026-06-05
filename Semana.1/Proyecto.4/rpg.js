const characters = []
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function createCharacter(name, classType) {
    const newCharacter = {
        name: name,
        classType: classType,
        level: 1,
        health: 100,
        attack: 10,
        defense: 5,
        mana: 50
    }

    if (classType === 'Warrior') {
        newCharacter.attack += 5
        newCharacter.defense += 5
    } else if (classType === 'Mage') {
        newCharacter.mana += 20
    } else if (classType === 'Archer') {
        newCharacter.attack += 3
        newCharacter.defense += 2
    }

    characters.push(newCharacter)
    console.log(`Personaje ${name} el ${classType} creado con éxito.`)
    showMenu()
}

function askClass(name) {
    console.log('Elige la clase del personaje:')
    console.log('1 - Warrior')
    console.log('2 - Mage')
    console.log('3 - Archer')

    rl.question('Ingrese el número de la clase: ', (option) => {
        let classType

        switch (option) {
            case '1':
                classType = 'Warrior'
                break
            case '2':
                classType = 'Mage'
                break
            case '3':
                classType = 'Archer'
                break
            default:
                console.log('Opción inválida. Por favor elige 1, 2 o 3.')
                return askClass(name)
        }

        createCharacter(name, classType)
    })
}

function askName() {
    rl.question('Ingrese el nombre del personaje: ', (name) => {
        askClass(name)
    })
}

function showCharacters() {
    if (characters.length === 0) {
        console.log('No hay personajes creados.')
        showMenu()
        return
    }

    console.log('Personajes creados:')
    characters.forEach((char, index) => {
        console.log(`${index + 1}. ${char.name} - ${char.classType} (Nivel ${char.level})`)
    })

    rl.question('¿Quieres elegir un personaje para subir de nivel? (s/n): ', (answer) => {
        const normalized = answer.trim().toLowerCase()
        if (normalized === 's' || normalized === 'si') {
            chooseCharacter()
        } else {
            showMenu()
        }
    })
}

function levelUp(character) {
    character.level += 1
    character.health += 20
    character.attack += 5
    character.defense += 3
    character.mana += 10
    console.log(`${character.name} ha subido al nivel ${character.level}!`)
}

function chooseCharacter() {
    if (characters.length === 0) {
        console.log('No hay personajes para elegir.')
        showMenu()
        return
    }

    console.log('Elige un personaje:')
    characters.forEach((char, index) => {
        console.log(`${index + 1}. ${char.name} - ${char.classType} (Nivel ${char.level})`)
    })

    rl.question('Ingrese el número del personaje: ', (input) => {
        const index = parseInt(input) - 1
        if (!isNaN(index) && index >= 0 && index < characters.length) {
            const selectedCharacter = characters[index]
            console.log(`Has elegido a ${selectedCharacter.name} el ${selectedCharacter.classType}.`)
            levelUp(selectedCharacter)
            showMenu()
        } else {
            console.log('Número de personaje inválido. Por favor intenta de nuevo.')
            chooseCharacter()
        }
    })
}

function showMenu() {
    console.log('Bienvenido al RPG! Elige una opción:')
    console.log('1 - Crear personaje')
    console.log('2 - Ver personajes')
    console.log('3 - Elegir personaje')
    console.log('4 - Salir')

    rl.question('Ingrese el número de la opción: ', (option) => {
        switch (option) {
            case '1':
                askName()
                break
            case '2':
                showCharacters()
                break
            case '3':
                chooseCharacter()
                break
            case '4':
                console.log('¡Hasta luego!')
                rl.close()
                break
            default:
                console.log('Opción inválida. Por favor elige 1, 2, 3 o 4.')
                showMenu()
        }
    })
}

showMenu()
