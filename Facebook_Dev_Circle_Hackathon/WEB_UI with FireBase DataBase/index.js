(function() {



    var config = {
        apiKey: "AIzaSyDqrvSXJLj8SxA3oaqaepbvBFsmn4WNMlc",
        authDomain: "sensor-dummy.firebaseapp.com",
        databaseURL: "https://sensor-dummy.firebaseio.com",
        projectId: "sensor-dummy",
        storageBucket: "sensor-dummy.appspot.com",
        messagingSenderId: "244501401650"
    };
    firebase.initializeApp(config);
      // Get Elements
        const preObject = document.getElementById('response1');
        const ulList = document.getElementById('list');
        
        // Create References
        const dbRefObject = firebase.database().ref().child('response1');
        const dbRefList = dbRefObject.child('hobbies');         
        // Sync object changes
        dbRefObject.on('value', snap => {let resp = (snap.val())
            w3.displayObject("id01",resp);
        });
        
        // dbRefObject.on('value', snap => {
        //     preObject.innerText = JSON.stringify(snap.val(), null, 3);
        //     console.log()
        // });
        
        dbRefList.on('child_added', snap => {
    
            const li = document.createElement('li');
            li.innerText= snap.val();
            ulList.appendChild(li);
        });
    
    
    
    
    
}());