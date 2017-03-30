
var parseYear = d3.time.format("%Y-%y").parse

/*function CSVtoChart(datafile, keyString, colorVal) {
	d3.csv(datafile, function(data) {

	    data = data.filter(function(row) {
	        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
	    })
	    var datavalues =[]
	    data.forEach(function(d) {
	    	d.year = parseYear(d.Academic_Yr);
	    	console.log(d.year)
	    	d.headcounts = +d.Headcounts;
	    	datavalues.push({x: d.year, y: d.headcounts})
	    })
	    console.log(data);

		nv.addGraph(function() {
			var chart = nv.models.lineChart()
		            .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
		            .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
		            // .transitionDuration(350)  //how fast do you want the lines to transition?
		            .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
		            .showYAxis(true)        //Show the y-axis
		            .showXAxis(true)        //Show the x-axis
		            // .x(function(d) {return d.year})
		            // .y(function(d) {return d.studentCount})
				;

				chart.xAxis     //Chart x-axis settings
		 	 	.axisLabel('Year')
		 	 	.tickFormat(function(d) { return d3.time.format('%Y')(new Date(d)); });

				chart.yAxis     //Chart y-axis settings
		  		.axisLabel('Number of students')
		  		// .tickFormat(d3.format('.02f'));

		  	// var myData = three_lines();
		  	var myData=[ {values: datavalues, key: keyString, color: colorVal }]
		  	console.log(myData)

		  	d3.select('#chart svg')
		  		.datum(myData)
		  		.call(chart);

		  	nv.utils.windowResize(function() { chart.update() });
				return chart;
		})
	});
}*

CSVtoChart("applied data.csv", "Applied",'#ff7f0e');
CSVtoChart("admitted data.csv", "Admitted", '#2ca02c');
CSVtoChart("SIRed data.csv", "Enrolled", '#7777ff');*/
	

d3.csv("applied data2.csv", function(line1) {
	
	var datavalues1 = []
    var datavalues2 = []
    var datavalues3 = []

    line1 = line1.filter(function(row) {
        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
    })
    
    line1.forEach(function(d) {
    	d.year = parseYear(d.Academic_Yr);
    	// console.log(d.year)
    	d.headcounts = +d.Headcounts;
    	datavalues1.push({x: d.year, y: d.headcounts})
    })
    console.log(line1);

    d3.csv("admitted data2.csv", function(line2) {
    	line2 = line2.filter(function(row) {
        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
	    })
	    line2.forEach(function(d) {
	    	d.year = parseYear(d.Academic_Yr);
	    	// console.log(d.year)
	    	d.headcounts = +d.Headcounts;
	    	datavalues2.push({x: d.year, y: d.headcounts})
	    })
	    console.log(line2);

		d3.csv("SIRed data2.csv", function(line3) {
	    	line3 = line3.filter(function(row) {
	        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
		    })
		    line3.forEach(function(d) {
		    	d.year = parseYear(d.Academic_Yr);
		    	// console.log(d.year)
		    	d.headcounts = +d.Headcounts;
		    	datavalues3.push({x: d.year, y: d.headcounts})
		    })
		    console.log(line3);
		})
	})

	

	nv.addGraph(function() {
		var chart = nv.models.lineChart()
	            .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
	            .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
	            // .transitionDuration(350)  //how fast do you want the lines to transition?
	            .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
	            .showYAxis(true)        //Show the y-axis
	            .showXAxis(true)        //Show the x-axis
	            // .x(function(d) {return d.year})
	            // .y(function(d) {return d.studentCount})
			;

			chart.xAxis     //Chart x-axis settings
	 	 	.axisLabel('Year')
	 	 	.tickFormat(function(d) { return d3.time.format('%Y')(new Date(d)); })
	 	 	;


			chart.yAxis     //Chart y-axis settings
	  		.axisLabel('Number of students')

	  		// chart.forceY([0,2000]);
	  		// .tickFormat(d3.format('.02f'));
	  	// var applied=[]
		// var admitted=[]
		// var enrolled=[]
	  	// var myData = three_lines(applied, admitted, enrolled);
	  	var myData=[ {values: datavalues3, key: 'Enrolled', color: '#7777ff'},
	  				 {values: datavalues1, key: 'Applied', color: '#ff7f0e'}, 
	  				 {values: datavalues2, key: 'Admitted', color: '#2ca02c'},
	  				 
	  			]
	  	console.log(myData)

	  	d3.select('#chart svg')
	  		.datum(myData)
	  		.call(chart)
	  		// .forceY([0,2000]);

	  	nv.utils.windowResize(function() { chart.update() });
			return chart;
	})
});

/*nv.addGraph(function() {
	var chart = nv.models.lineChart()
            .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
            .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
            // .transitionDuration(350)  //how fast do you want the lines to transition?
            .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
            .showYAxis(true)        //Show the y-axis
            .showXAxis(true)        //Show the x-axis
            // .x(function(d) {return d.year})
            // .y(function(d) {return d.studentCount})
		;

		chart.xAxis     //Chart x-axis settings
 	 	.axisLabel('Year')
 	 	.tickFormat(function(d) { return d3.time.format('%Y')(new Date(d)); });

		chart.yAxis     //Chart y-axis settings
  		.axisLabel('Number of students')
  		// .tickFormat(d3.format('.02f'));
  	
  	var myData = three_lines();
  	// var myData=[ {values: datavalues, key: 'Applied' }]
  	console.log(myData)

  	d3.select('#chart svg')
  		.datum(myData)
  		.call(chart);

  	nv.utils.windowResize(function() { chart.update() });
		return chart;
})

function three_lines() {
	var applied=[], admitted=[], enrolled=[];
	
	d3.csv("applied data.csv", function(data) {
		datavalues =[]
	    data = data.filter(function(row) {
	        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
	    })
	    data.forEach(function(d) {
	    	d.year = parseYear(d.Academic_Yr);
	    	// console.log(d.year);
	    	d.headcounts = +d.Headcounts;
	    	datavalues.push({x: d.year, y: d.headcounts});
	    })
	   	for (var i = 0; i < datavalues.length; i++) {
	   		applied.push(datavalues[i]);
	   	}
	    // series.push({values: applied, key: 'Applied'})
	})
	 console.log(applied);
	d3.csv("admitted data.csv", function(data) {

	    data = data.filter(function(row) {
	        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
	    })
	    data.forEach(function(d) {
	    	d.year = parseYear(d.Academic_Yr);
	    	// console.log(d.year)
	    	d.headcounts = +d.Headcounts;
	    	admitted.push({x: d.year, y: d.headcounts})
	    })
	    // console.log(admitted);
	    // series.push({values: admitted, key: 'Admitted'})
	})

	d3.csv("SIRed data.csv", function(data) {

	    data = data.filter(function(row) {
	        return row['Ethnicity'] == 'Asian' && row['Gender'] == 'Female' && row['Derived Residency'] == 'CA Resident' && row['College'] == 'Clg of Engineering';
	    })
	    data.forEach(function(d) {
	    	d.year = parseYear(d.Academic_Yr);
	    	// console.log(d.year)
	    	d.headcounts = +d.Headcounts;
	    	enrolled.push({x: d.year, y: d.headcounts})
	    })
	    console.log(enrolled);
	})

	return [
		{
			values: applied,
			key: 'Applied'
		},
		{
			values: admitted,
			key: 'Admitted'
		},
		{
			values: enrolled,
			key: 'Enrolled'
		}
	];
	
	// return [{ values: applied, key: 'Applied', seriesIndex: 0 }];
		    // { values: admitted, key: 'Admitted' },
			// { values: enrolled, key: 'Enrolled' }
	
}*/
