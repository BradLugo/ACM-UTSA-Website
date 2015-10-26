var site = angular.module('ACM-UTSA', ['ui.router']);

site.controller('NavigationController', function($scope, $location) {
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
});