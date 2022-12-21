function edit_action(task_id){
    if (document.getElementById(`edit${task_id}`).innerHTML == 'Edit'){
        document.getElementById(`edit${task_id}`).innerHTML = 'Save'
        document.getElementById(`task_body_${task_id}`).disabled = false
    }
    else {
        document.getElementById(`edit${task_id}`).innerHTML = 'Edit'
        document.getElementById(`edited_form_${task_id}`).submit()
    }
}
