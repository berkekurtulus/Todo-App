const addTaskBtn = document.getElementById('add_task_btn');
const taskInput = document.getElementById('task_input');
const taskDateInput = document.getElementById('task_date');
const taskList = document.getElementById('task_list');
const completedList = document.getElementById('completed_list');

addTaskBtn.addEventListener('click', function() {
    const taskText = taskInput.value;
    const taskDate = taskDateInput.value;

    if (taskText === "" || taskDate === "") {
        alert("Please fill in all fields!");
        return;
    }
    const todayDate = "2026-07-06";
    let status = "pending";
    if(taskDate === todayDate){
        status = "today"
    }
    else if (taskDate < todayDate){
        status = "overdue"
    }
        
    const li = document.createElement('li');
    li.innerHTML = `<input type="checkbox" class="task_check">
        <span>${taskText}</span>
        <time>(${status}) ${taskDate}</time>
        <button type="button" class="edit_btn">Edit</button>
        <button type="button" class="delete_btn">Delete</button>
    `;
    taskList.appendChild(li);

    taskInput.value = "";
    taskDateInput.value = "";
    
    });

taskList.addEventListener('click', function(event) {
   
     const selectedRow = event.target.parentElement;

    if (event.target.className === 'delete_btn') {
        selectedRow.remove();
    }

    else if (event.target.className === 'task_check') {
        completedList.appendChild(selectedRow);
    }

    else if (event.target.className === 'edit_btn') {
        const oldText = selectedRow.querySelector('span').innerText;
        taskInput.value = oldText;
        selectedRow.remove();
    }
});
