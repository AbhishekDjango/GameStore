function Preloader() {
  var view = View.getInstance();

  var loadingPercentage;

  var imageSources;
  var soundSources;

  var that = this;

  this.init = function() {
    loadingPercentage = view.create('div');

    view.addClass(loadingPercentage, 'loading-percentage');
    view.setHTML(loadingPercentage, '0%');
    view.appendToBody(loadingPercentage);

    imageSources = {
      1: '/static/images/back-btn.png',
      2: '/static/images/bg.png',
      3: '/static/images/bullet.png',
      4: '/static/images/clear-map-btn.png',
      5: '/static/images/coin.png',
      6: '/static/images/delete-all-btn.png',
      7: '/static/images/editor-btn.png',
      8: '/static/images/elements.png',
      9: '/static/images/enemies.png',
      10: '/static/images/flag-pole.png',
      11: '/static/images/flag.png',
      12: '/static/images/start-screen.png',
      13: '/static/images/grid-large-btn.png',
      14: '/static/images/grid-medium-btn.png',
      15: '/static/images/grid-small-btn.png',
      16: '/static/images/grid.png',
      17: '/static/images/lvl-size.png',
      18: '/static/images/mario-head.png',
      19: '/static/images/mario-sprites.png',
      20: '/static/images/powerups.png',
      21: '/static/images/save-map-btn.png',
      22: '/static/images/saved-btn.png',
      23: '/static/images/slider-left.png',
      24: '/static/images/slider-right.png',
      25: '/static/images/start-btn.png'
    };

    that.loadImages(imageSources);
  };

  this.loadImages = function(imageSources) {
    var images = {};
    var loadedImages = 0;
    var totalImages = 0;

    for (var key in imageSources) {
      totalImages++;
    }

    for (var key in imageSources) {
      images[key] = new Image();
      images[key].src = imageSources[key];

      images[key].onload = function() {
        loadedImages++;
        percentage = Math.floor(loadedImages * 100 / totalImages);

        view.setHTML(loadingPercentage, percentage + '%'); //displaying percentage

        if (loadedImages >= totalImages) {
          view.removeFromBody(loadingPercentage);
          that.initMainApp();
        }
      };
    }
  };

  this.initMainApp = function() {
    var marioMakerInstance = MarioMaker.getInstance();
    marioMakerInstance.init();
  };
}

window.onload = function() {
  var preloader = new Preloader();
  preloader.init();
};
