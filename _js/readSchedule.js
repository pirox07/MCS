var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        var data = this.response;
        var str = data.ScheduleExpression;
        var utc_hh = Number(str.substr(8,2));

        var jst_hh;
        if (utc_hh <= 14){
          jst_hh = utc_hh + 9;
        } else {
          jst_hh = utc_hh - 15;
        }

        var hh = ('00' + jst_hh).slice(-2);

		document.getElementById("time").value = hh + ":" + str.substr(5,2);
//        console.log(data);
//        console.log(str);
//        console.log(hhmm);
        };
};


xhr.responseType = 'json';

xhr.open('GET', 'https://mcs.piroshi07.com/getSchedule', true);
xhr.send();
