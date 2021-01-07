<p style="font-size:30px">


<h2>Smart doorbell</h2>
  

Student name: Diana Morena Tifrea Student ID: 15721225

Configure an Amazon Dash Button as a doorbell with the help of a Raspberry Pi using Pushover.

<h2>Setting up the Dash Button</h2>
I have used an <a href="https://en.wikipedia.org/wiki/Amazon_Dash"> Amazon Dash </a> - it was possible to purchase this button for 5 GBP and hack it to work as a typical smart button, and not for its intended purpose. Sadly, Amazon has stopped selling these buttons in 2019 and then proceeded to disable some of the ones that were already active.

After receiving the button, I turned on bluetooth and wifi on my phone, initialized the button by pressing it for 6 secs, then followed the on-screen instructions in the Amazon App.
  
When it asks to choose a product, do NOT choose a product to order.
Close the app completly. The button now has access to the wifi.

Since it's now connected to the WiFi, I was able to login to the router and see the mac address it used to connect.
I needed the MAC address so I can later filter out any other packets from the network, and only trigger the function to call the Cloud API when the dash button is pressed, and not if any other UDP requests are appearing in the sniffer.

<h2>Setting up the Cloud messaging platform</h2>
I have created an app in <a href="https://pushover.net/"> Pushover </a> called doorbell.
I have chosen Pushover as it's a one time purchase. 

<h2>Creating a Python script to interact with the Pushover service</h2>

I created a python script were I have placed the MAC address of my Amazon dash button and the API and token user from Pushover.

Using the 

When the "doorbell" Amazon dash button is pressed I will get a notification throungh Pushover on my smartphone.
Through the app I can also track time and date when the doorbell was rang or the door was opened.

I have used the Accelerometer to detect<a href="https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8/"> movement </a> and notify me through Pushover when the door is open.

I have also used the Temperature, Humidity and Pressure sensors from the Sense Hat to display the <a href="https://www.instructables.com/Weather-Display-With-Sense-Hat/"> Temperature, Humidity and Pressure </a> once the door is opened.
Also a <a href="https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/3"> message </a> is displayed on the smart hat when the door is opened "Door is open" and Temperature, Humidity and Pressure results.



















