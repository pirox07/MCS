var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        var InfoCron = this.response;
        var HHMM = InfoCron.substr(8,2)+":"+InfoCron.substr(5,2)+"だよーん"
		document.write(HHMM)

        console.log(InfoCron)
        console.log(HHMM)        
        };
};


xhr.responseType = 'json';
xhr.open('GET', 'https://kr4ny6a3b1.execute-api.us-east-1.amazonaws.com/dev/mcs-get-schedule', true);
xhr.send();