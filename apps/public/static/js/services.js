'use strict';

publicApp.factory('Name', function () {
    var name = 'Recipe Organizer';

    return {
        getName: function () {
            return name;
        }
    }
});