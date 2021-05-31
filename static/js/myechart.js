  $.ajax({
    type: "get",
    url: "{%url 'tieta:apiecharts'%}",
    success: function(data) {
      chart1fun(data)
      chart2fun(data)
      chart3fun(data)
    },
    // 指定图表的配置项和数据
    error: function() {
      alert('Error: ajax 请求出错！')
    }
  });


  var myChart1 = echarts.init(document.getElementById('chart1'));
  function chart1fun(data) {
    option = {
      title: {
        left: 'center',
        text: '年租金统计(万元)'
      },
      tooltip: {},
      xAxis: {
        data: data['营服']
      },
      yAxis: {},
      series: [{
        name: '年租金(万元)',
        type: 'bar',
        data: data['服务费'],
        itemStyle:{
            normal:{
                label:{
                    show:true,
                    position:'top',
                    textStyle:{
                        color:'#6c757d',
                        fontSize:16
                    }
                }
            }
        }
      }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart1.setOption(option);
//自适应div大小
window.addEventListener("resize",function(){
    myChart1.resize();
});
  }
  var myChart2 = echarts.init(document.getElementById('chart2'));
function chart2fun(data){
  // 指定图表的配置项和数据
  option = {
    title: {
        text: "铁塔站址个数",
        subtext: '按站址维度',
        left: 'center',
},
    series: [{
      name: '访问来源',
      type: 'pie',
      radius: '60%',
      roseType: 'angle',
      data: data['站址数'],
 itemStyle:{
            normal:{
                  label:{
                    show: true,
                    formatter: '{b}:{c}个 '
                  },
                  labelLine :{show:true}
                }
            }
    }]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart2.setOption(option);
//自适应div大小
window.addEventListener("resize",function(){
    myChart2.resize();
});
}

  var myChart3 = echarts.init(document.getElementById('chart3'));
function chart3fun(data){
  // 指定图表的配置项和数据
    option = {
      title: {
        left: 'center',
        text: '年均租金(元)'
      },
      tooltip: {},
      xAxis: {
        data: data['营服']
      },
      yAxis: {},
      series: [{
        name: '年租金(元)',
        type: 'bar',
        data: data['年均'],
        itemStyle:{
            normal:{
                label:{
                    show:true,
                    position:'top',
                    textStyle:{
                        color:'#6c757d',
                        fontSize:16
                    }
                }
            }
        }
      }]
    };

  // 使用刚指定的配置项和数据显示图表。
  myChart3.setOption(option);
//自适应div大小
window.addEventListener("resize",function(){
    myChart3.resize();
});
}