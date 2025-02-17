from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return """<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
     <style>
     a{
      font-size: 20px;
      color: white;
     }
body {
  font-family: 'Lato', sans-serif;
}

.overlay {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0, 0.9);
  overflow-x: hidden;
  transition: 0.5s;
}

.overlay-content {
  position: relative;
  top: 25%;
  width: 100%;
  text-align: center;
  margin-top: 30px;
}

.overlay a {
  padding: 8px;
  text-decoration: none;
  font-size: 36px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.overlay a:hover, .overlay a:focus {
  color: #f1f1f1;
}

.overlay .closebtn {
  position: absolute;
  top: 20px;
  right: 45px;
  font-size: 60px;
}

@media screen and (max-height: 450px) {
  .overlay a {font-size: 20px}
  .overlay .closebtn {
  font-size: 40px;
  top: 15px;
  right: 35px;
  }
}
</style>
    <style>
/* Style the body */
body {
  font-family: Arial;
  margin: 0;
}

/* Header/Logo Title */
.header {
  padding: 60px;
  text-align: center;
  background: #1abc9c;
  color: white;
  font-size: 30px;
}
 button:hover{
          background: darkcyan;
          color: white;
          transform: translateY(-10px);
          transition: transform 0.3s ease 0;
        }
</style>
	
	<style>
		body,
		html {
			height: 100%;
			margin: 0;
			font-family: Arial, Helvetica, sans-serif;
		}

		.hero-image {
			background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("space.jpeg");
			height: 100%;
			background-position: center;
			background-repeat: no-repeat;
			background-size: cover;
			position: relative;
		}

		.hero-text {
			text-align: center;
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			color: white;
		}

		.hero-text button {
			border: none;
			outline: 0;
			display: inline-block;
			padding: 15px 25px;
			color: black;
			background-color: #ddd;
			text-align: center;
			cursor: pointer;
		}

		.hero-text button:hover {
			background-color: #555;
			color: white;
		}
	</style>
    <title>Minecraft(basic tutorials)</title>
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body style="background-repeat: no-repeat;background-size: 100% 100%;background-attachment: fixed;" background="/static/oip.jpeg"
 text="#ffffff">
    <font face="Harlow Solid">
    <div class="hero-image">
		<div class="hero-text">
			<div style="border: 4px solid Red">
        <div class="header">
				<h1 align="center" >MINECRAFT</h1>
			<h2 align="center" > A Snadbox video game </h2>
        </div>
      </div>
		</div>
	</div>
      <div style="border: 4px solid purple">
    <h2 align ="center">Minecraft is the most complicated game to make in the world</h2>
    <h2 align ="center"> It was made by Markus Persson or Notch.</h2>
    <h2 align="center"> In the game, there's an aim, the aim is to defeat a powerful creature called the ENDER DRAGON; the most powerful creature ever lived in minecraft. </h2>
      </div>
       <br>
    <br>
      <br>
       <br>
    <br>
      <br>
      <div style="border: 4px solid purple">
    <h2 align ="center"> To defeat the Ender Dragon, you must go to a dimension called the End, no not the end which means a final part of something, especially a period of time, an activity, or a story; it's a dimension, this dimension looks more likly space, except, there are no stars, and you can breathe there.There's also a thing  </h2>
      </div>
      <br>
    <br>
      <br>
       <br>
    <br>
      <br>
       <br>
    <br>
      <br>
      <h2 align="center"> First you spawn (a spawn is the point where you start, means,where you are standing after creating a new world)
        in the overworld (Earth), second you must gather wood to make a crafting table( the table where making thing example: sword, pickaxe, axe, and may more); after that, you make a pickaxe and mining stone with it, then you can make all the things that are given in the above example(Remember, you are making it out of stone). </h2>
       <br>
    <br>
      <br>
       <br>
    <br>
      <br>
      <h2 align="center"> Then you can mine iron which is found in between levels Y=72 and Y=-64. Now, must be wondering, how to know if we're there in that level.
        Well, you should click the F3 function key on the keyboard. And you'll get something like this in the below image</h2>
       <br>
    <br>
      <br>
       <br>
    <br>
      <br>
      <center> <img src="/static/debug.png" width="500" height="300"> </center>
      <br>
    <br>
      <br>
       <br>
    <br>
      <h2 align="center"> after getting iron, you smelt it in a furnace, to get iron ingot, which can be used to make armor, tools, weapons, etc. If you are lucky, you can find Diamonds! which can be also used to make armor, tools, weapons, etc. Diamond Ore frequently appears between layers 5-16, but it is most abundant on layer 12.
      </h2>
       <br>
    <br>
      <br>
       <br>
    <br>
      <br> <br>
    <br>
      <br>
       <br>
    <br>
      <br>
      <h2 align="center"> That's it for today! </h2>

      <center> <svg height="300" width="500">
  <defs>
    <linearGradient id="grad1" x1="10%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"
      style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%"
      style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <ellipse cx="100" cy="70" rx="85" ry="55" fill="url(#grad1)" />
  <text fill="#0000ff" font-size="35" font-family="Verdana"
  x="50" y="80">THANK YOU</text>
</svg>  
<h2>Next Page</h2>
<button class="normal"><a href="/minecraft2"><button>Next Page</button></a></button>
     </center>   
      
      </font>


  </body>
</html>"""
  
   

@app.route('/minecraft4')
def minecraft4():
  page = ""
  f = open("minecraft4.html", "r")
  page = f.read()
  f.close()  
  return page

@app.route('/minecraft3')
def minecraft3():
  page = ""
  f = open("minecraft3.html", "r")
  page = f.read()
  f.close()  
  return page

@app.route('/minecraft2')
def minecraft2():
  page = ""
  f = open("mecraft2.html", "r")
  page = f.read()
  f.close()  
  return page


@app.route('/endcity')
def end_city():
  page = ""
  f = open("endcity.html", "r")
  page = f.read()
  f.close()  
  return page


app.run(host='0.0.0.0', port=81)
