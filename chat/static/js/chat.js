const text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
    '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
    '{message}' +
    '</div>';

let userState = ''

//                    <span style="color: ${online ? 'green' : 'red'}; float: right">${online ? 'online' : 'offline'}</span>

const userDiv = (senderId, receiverId, name, online, image) =>
    (`<a href="/chat/${senderId}/${receiverId}" id="user${receiverId}" class="collection-item row">
                    <img src='/static/${image}' class="col s4 rounded-circle" width='40'>
                    <div class="col s8">
                    <span class="title" style="font-weight: bolder">${name}</span>

                    </div>
                </a>`)

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}

function send(sender, receiver, message) {
    $.post('/api/messages', '{"sender": "' + sender + '", "receiver": "' + receiver + '","message": "' + message + '" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        $('#board').append(box);
        scrolltoend();
    })
}

function receive() {
    $.get('/api/messages/' + sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);
                scrolltoend();
            }
        }
    })
}

function getUsers(senderId, callback) {
    return $.get('/api/users', function (data) {
//        console.log(JSON.stringify(data))
//        console.log('userstate',userState)
        users = []
        faculties=[]
        data.map((_)=>{
            if(_.id != null){
                users.push(_)
            }
            else{
                faculties.push(_)
            }
        })
        for(user of users){
            for(faculty of faculties){
                if(user.username == faculty.faculty_id){
                    user.name = faculty.faculty_name
                    user.image = faculty.image.split('/')[4]
                }
            }
            console.log('modified user',user)
        }

        console.log('users',users,'facultues',faculties)


        if (userState !== JSON.stringify(users)) {
            userState = JSON.stringify(users);
            const doc = users.reduce((res, user) => {
            console.log('res',res,'user',user)
                if (user.id === senderId) {
                    return res
                } else {
                    return [userDiv(senderId, user.id, user.name, user.online, user.image), ...res]
                }
            }, [])
            callback(doc)
        }
    })
}

function register(username, password) {
    $.post('/api/users', '{"username": "' + username + '", "password": "' + password + '"}',
        function (data) {
            console.log(data);
            window.location = '/';
        }).fail(function (response) {
            $('#id_username').addClass('invalid');
        })
}