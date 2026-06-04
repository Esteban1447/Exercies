
const readline = require('readline');
const tasks = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function showMenu() {
  console.log('\nTo-Do List');
  console.log('1. Add Task');
  console.log('2. View Tasks');
  console.log('3. Delete Task');
  console.log('4. Exit');     }

function addTask() {
    rl.question('enter a task: ', (task) => {
        tasks.push(task);
        console.log('Task added!');
        showMenu();
        rl.prompt();
    });
}

function deleteTask() {
    if (tasks.length === 0) {
        console.log('No tasks to delete.');
        showMenu();
        rl.prompt();
        return;
    }

    function promptDelete() {
        console.log('\nTasks:');
        tasks.forEach((task, i) => {
            console.log(`${i + 1}. ${task}`);
        });
        rl.question('Enter the task number to delete (or press Enter to return): ', (input) => {
            const trimmed = input.trim();
            if (trimmed === '') {
                showMenu();
                rl.prompt();
                return;
            }
            const index = parseInt(trimmed) - 1;
            if (!isNaN(index) && index >= 0 && index < tasks.length) {
                tasks.splice(index, 1);
                console.log('Task deleted!');
                if (tasks.length === 0) {
                    console.log('No tasks left.');
                    showMenu();
                    rl.prompt();
                    return;
                }
                promptDelete();
            } else {
                console.log('Invalid task number. Please try again.');
                promptDelete();
            }
        });
    }

    promptDelete();
}

function viewTasks() {
    if (tasks.length === 0) {
        console.log('No tasks added yet.');
    } else {
        console.log('Tasks:');
        tasks.forEach((task, index) => {
            console.log(`${index + 1}. ${task}`);
        });
    }   }

function main() {
    showMenu();
    rl.prompt();
}

rl.on('line', (input) => {
    switch (input.trim()) {
        case '1':
            addTask();
            break;
        case '2':
            viewTasks();
            showMenu();
            break;
        case '3':
            deleteTask();
            break;
        case '4':
            console.log('Exiting...');
            rl.close();
            break;
    }
});

main();