
This application is hosted on: http://134.122.57.252/

# Features:

It allows you to:
  - Create a new stockreading with an expiration date
  - See all the current stockreadings
  - see the expired stockreadings


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF
  
# Async mechanism

To be able to use this application offline (collect and insert new datas inside the database),
i would have created a local database for the only offline purpose.

The second databse, mutch lighter and installed on the device app, would receive temporary
datas if the offline statement is validate.

Once the network turns on again, the mobile app should request the permanent database to
compare datas and make an updates of the last inserted products.

