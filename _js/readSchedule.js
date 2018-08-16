var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        var data = this.response;
        var str = data.ScheduleExpression;
        var hhmm = str.substr(8,2) + ":" + str.substr(5,2);
		document.getElementById("time").value = hhmm;
//        console.log(data);
//        console.log(str);
//        console.log(hhmm);
        };
};


xhr.responseType = 'json';
xhr.open('GET', 'https://kr4ny6a3b1.execute-api.us-east-1.amazonaws.com/dev/mcs-get-schedule', true);
xhr.send();