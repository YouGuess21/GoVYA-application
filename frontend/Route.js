import {BrowserRouter as Router, Switch, Route } from ‘react-router-dom’;

import { LandingPage} from './App.jsx';

export const Route = () => {
    return (
        <Router>
            <Switch>
                <Route path="/">
                    <LandingPage />
                </Route>
            </Switch>
        </Router>
    )
}


