'use strict';

publicApp.controller('HelloController', ['$scope', 'Name', function($scope, Name) {
    $scope.name = Name.getName();
}]);

publicApp.controller('LoginController', ['$scope', function($scope) {
    $scope.hasError = function (field, validation) {
        if (validation) {
            return $scope.loginForm[field].$dirty && scope.loginForm[field].$error[validation];
        }
        return $scope.loginForm[field].$dirty && $scope.loginForm[field].$invalid;
    };
}])