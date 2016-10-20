!function() {
	
	  var department = ["Account", "Administrative",  "Animal Control", "City", "Construction", "Court",  "Executive","Fire", "Labourer", "Medical", "Municipal",  "Police", "Recreation", "Transit"];
	
	  var dropDown = d3.select("#filter").append("select").attr("name", "department-list");
	  
	  var optionsk = dropDown.selectAll("option")
           .data(["Select"].concat(department))
         .enter()
           .append("option");
		  optionsk.text(function (d) { return d; })
       .attr("value", function (d) { return d; });
					
	  dropDown.on("change", function() {
		  dataFile = 'data/SF' + this.value + '.json';
		  
		  d3.select('#ep').remove();
		  
		  defaultDistribution('d3-tip', dataFile);
		  d3.select('#boxplotTitle').text( 'Distribution of Average Base Pay for Men & Women by Title for '+this.value+'  Department for 2014');
	  
     
      });
   // module container
   var boxPlotFunctions = {};

   boxPlotFunctions.removeTooltip = removeTooltip;
   function removeTooltip (d, i, element) {
      if (!$(element).popover) return; 
      $('.popover').each(function() {
         $(this).remove();
      }); 
   }

   boxPlotFunctions.showTooltip = showTooltip;
   function showTooltip (d, i, element, constituents, options) {
      if (!$(element).popover) return; 
      $(element).popover({
         placement: 'auto top',
         container: '#' + constituents.elements.domParent.attr('id'),
         trigger: 'manual',
         html : true,
         content: function() { 
            var identifier = options.data.identifier && d[options.data.identifier] ?
               d[options.data.identifier] : 'undefined';
            var value = options.axes.y.label && d[options.axes.y.label] ?
               options.axes.y.tickFormat(d[options.axes.y.label]) : '';

            var message = "<span style='font-size: 11px; text-align: center;'>";
            message += d[options.data.identifier] + ': ' + d[options.axes.y.label] + "</span>"; 

            return message;
         }
      });
      $(element).popover('show');
   }

   boxPlotFunctions.defineTooltip = defineTooltip;
   function defineTooltip(constituents, options, events) {
       var tip = d3.tip().attr('class','explodingBoxplot tip')
            .direction('n')
            .html(tipFunction)

       function tipFunction(d) {
          var color = options.data.color_index && d[options.data.color_index] ?
             constituents.scales.color(d[options.data.color_index]) : 'blue';
          var identifier = options.data.identifier && d[options.data.identifier] ?
             d[options.data.identifier] : 'undefined';
          var value = options.axes.y.label && d[options.axes.y.label] ?
             options.axes.y.tickFormat(d[options.axes.y.label]) : '';
          var message = ' <span style="color:' + color + '">' + identifier + 
                        '</span><span style="color:#DDDDDD;" > : ' + value + '</span>';
          return message;
       }

       events.point.mouseover = tip.show;
       events.point.mouseout = tip.hide;

       if (constituents.elements.chartRoot) constituents.elements.chartRoot.call(tip);
   }

   boxPlotFunctions.defaultDistribution = defaultDistribution;
   function defaultDistribution(tooltip, dataFile) {
	  
		  		
      var default_distributions = dataFile;
      var container = d3.select('#pointDistributions');
		//console.log("s");
      d3.json(default_distributions, function(error, result) {
		  //console.log("suc");
         if (error || !result) return;
		//console.log("success");
         var xbp = explodingBoxplot();
         boxPlotFunctions.xbp = xbp;

         if (tooltip) {
            if (tooltip == 'popover') xbp.events({ 'point': { 'mouseover': showTooltip, 'mouseout': removeTooltip } });
            if (tooltip == 'd3-tip') xbp.events({ 'update': { 'ready': defineTooltip } });
         }

         xbp.options(
            { 
               id:   'demo',
               data: { 
                  group: 'title', 
				  color_index: 'Gender',
                  //color_index: 'title',
                  identifier: 'JobTitle'
               }, 
               width: 900, 
               height: 680, 
               axes: { 
                  x: { label: 'Title' }, 
                  y: { label: 'BasePay' } 
               } 
            }
         );

         xbp.data(result.data);
         container.call(xbp);
         xbp.update();

      });
   }

 

   if (typeof define === "function" && define.amd) define(boxPlotFunctions); else if (typeof module === "object" && module.exports) module.exports = boxPlotFunctions;
   this.boxPlotFunctions = boxPlotFunctions;

}();
