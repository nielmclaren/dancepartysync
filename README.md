Dance Party Synchronization
---------------------------

Open sync.html to see the resulting dance party.

Grabbed a few animated GIFs tagged "dance party" plus some pendulums from Wikipedia. The beat of each GIF was recorded and synchronized with other GIFs so it would look like a proper dance party instead of dancing extras on a set. This turned out to be harder than I thought.

A Python script pulled apart GIFs and reassembled each frame into a filmstrip. This image is then used like a CSS sprite so Javascript could control the framerate and timing.

record.html is used to get the user to record the beat of the animation. The resulting JSON object can be added to sync.html to add that dancer to the party.

Many GIFs won't work just because the animation doesn't have a good beat.

Original animated GIFs from [Tumblr](http://www.tumblr.com/tagged/gif-dance-party) and [Wikipedia](http://www.wikipedia.org).
