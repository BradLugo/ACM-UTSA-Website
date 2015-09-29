site.config(function($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        });

    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: '../views/home.html'
        })
        .state('about', {
            url: '/about',
            templateUrl: '../views/about.html'
        })
        .state('404', {
            url: '/404',
            templateUrl: '../404.html'
        });

        $urlRouterProvider.when('/index', '/');
        $urlRouterProvider.when('/home', '/');
        $urlRouterProvider.otherwise('/404');
});