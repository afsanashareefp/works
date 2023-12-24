var subjectObject = {
    "Commerce": {
      "BBA": ["Tags", "Links", "Images", "Tables", "Lists", "colors", "Attributes", "Classes", "input", "Iframes", "Div/Span", "Metatags", "Headings", "Favions"],
      "BCom": ["padding", "Margins", "Borders", "Display", 'Icons', "Units", 'z-index', 'Pseudo-class', "Pseudo-element", "!important", "Text-Effect", "Mart-Function", "Transitions", "Aminations", "Transform", "Variables", "Flexbox", 'Grid', 'Masking', 'Media Query'],

    },
    "Computer science": {
      "BCA": ['Routing and HTTP Methods', 'Middleware', 'Cookies', 'REST APIs', 'Scaffolding', 'Database Connectivity', 'Templating'],
      "CS": ['REPL', 'package manager', 'callbacks', 'event loop', 'os', 'path', 'query string', 'cryptography', 'debugger', 'URL', 'DNS', 'Net', 'UDP', 'process', 'child processes', 'buffers', 'streams', 'file systems', 'global objects', 'web modules']
    },
    "Language":{
      "B A Malayalam" : ['Documents', 'Collections', 'Compass', 'Replica Sets', 'Sharding', 'Indexes', 'Aggregation Pipelines', 'MongoDB Cloud'],
      "BSc Hindi" : ['Create TABLE', 'Insert Data Into Table', 'Select Query', 'Table Constraints', 'And oR and NOT Operator', 'IN Operator', 'LIKE Operator', 'MySQL Aggregate Functions'],
    }

}


window.onload = function(){
    var first = document.getElementById('first')
    var second = document.getElementById('second')


    for(var x in subjectObject){
        // console.log(x);
        first.options[first.options.length] = new Option(x)
    }

    first.onchange = function(){
        second.length = 1

        second.style.display = 'block'

        for(var y in subjectObject[this.value]){
            // console.log(y);
            second.options[second.options.length] = new Option(y)
        }
    }




}