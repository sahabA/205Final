<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Women making 16% less than men</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

	
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet">

	<script src="http://d3js.org/d3.v3.js"></script>
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.6.7/d3-tip.min.js"></script>

	 <script src="http://code.jquery.com/jquery-1.8.3.min.js" type="text/javascript" charset="utf-8"></script>



</head>

<body>
			<div id="table1"></div>
        
</body>
     
        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>w209 project, Spring 2016 by Sahab Aslam</p>
                </div>
            </div>
        </footer>

    </div>
    <!-- /.container -->

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>
	  <script src="js/jquery.min.js"></script>
    <script type="text/javascript">
		var circleData2 = [
		 { "cx": 500, "cy": 360, "radius": 125, "color" : "#E85371" , "text": "w"},
		 { "cx": 1000, "cy": 360, "radius": 125, "color" : "#587696", "text": "m" }];
		 
		var textData2 = [
		{ "x": 190, "y": 150,   "text": "For a government job in SF, the average pay gap is: ", "fsize" :50},
		 { "x": 410, "y": 380,   "text": "$0.84", "fsize" :70},
		 { "x": 910, "y": 380,  "text": "$1.00", "fsize" :70 },
			 {"x": 410, "y": 610,  "text": "Women", "fsize" :50},
			 {"x": 950, "y": 610,  "text": "Men", "fsize" :50}
		 ];

				var guideC2 = d3.select("#table1")
							.append("svg")
						.attr("width",1400)
						  .attr("height",1300);
				var circles2 = guideC2.selectAll("circle")
								.data(circleData2)
								   .enter()
								  .append("circle");
				var circleAttributes2 = circles2
								.attr("cx", function (d) { return d.cx; })
								.attr("cy", function (d) { return d.cy; })
								.attr("r", function (d) { return d.radius; })
								.style("stroke", function (d) { return d.color; })
								.style("fill", function (d){ if (d.text == "w"){ return "url(#grad)";} return "#b2df8a"})
								.attr("stroke-width", 20);	
								
				var t2 = guideC2.selectAll("text")
								.data(textData2).enter()
								  .append("text");
				var	gt2 = t2.attr('y', function (d) { return d.y; } ). attr('x', function (d) { return d.x; } ).text(function (d) { return d.text; }).style("stroke", "black").style("font-size", function (d) { return d.fsize; });
				
				 var grad = guideC2.append("defs").append("linearGradient").attr("id", "grad")
			.attr("x1", "0%").attr("x2", "0%").attr("y1", "100%").attr("y2", "0%");
		grad.append("stop").attr("offset", "84%").style("stop-color", "#b2df8a");
		grad.append("stop").attr("offset", "84%").style("stop-color", "white");
	</script>
	
	<script src="js/jquery.tpsy.js" type="text/javascript" charset="utf-8"></script>
	
      <script src="https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.6.7/d3-tip.min.js"></script>


</body>

</html>
<?php header( "refresh:3;url=visualization.html" ); ?>