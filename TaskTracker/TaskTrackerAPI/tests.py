import requests

def test_create_task():
    r = requests.post('http://127.0.0.1:8000/v1/tasks/create/', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get('http://127.0.0.1:8000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 4

def test_get_task():
    r = requests.get('http://127.0.0.1:8000/v1/tasks/1')
    assert isinstance(r.json(),dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 4

def test_update_task():
    r = requests.put('http://127.0.0.1:8000/v1/tasks/1/update/', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content

def test_delete_task():
    r = requests.delete('http://127.0.0.1:8000/v1/tasks/1/delete/')
    assert not r.content

def test_add_bulk_task():
    tasks_to_add = [
        {"title": "Task 1", "is_completed": False},
        {"title": "Task 2", "is_completed": False}
    ]
    
    r = requests.post('http://127.0.0.1:8000/v1/tasks/bulk-add/', json=tasks_to_add)
    
    assert r.status_code == 201  
    assert isinstance(r.json(), list)  
    assert len(r.json()) == len(tasks_to_add)  
    for task in r.json():
        assert isinstance(task["id"], int)  
        assert isinstance(task["title"], str) 
        assert isinstance(task["is_completed"], bool)  

def test_delete_bulk_task():
    tasks_to_delete = [2, 3] 

    r = requests.delete('http://127.0.0.1:8000/v1/tasks/bulk-delete/', json={"tasks": tasks_to_delete})

    assert r.status_code == 204 
    
    assert r.text == ""  
    
    remaining_tasks = requests.get('http://127.0.0.1:8000/v1/tasks/').json()
    for task_id in tasks_to_delete:
        assert task_id not in [task["id"] for task in remaining_tasks["tasks"]] 
 
