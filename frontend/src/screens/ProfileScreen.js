import React, { useContext } from 'react';
import { Store } from '../Store';

export default function ProfileScreen() {
  return (
    <div className="container small-container">
      <Helmet>
        <title>User Profile</title>
      </Helmet>
      <h1 className="my-3">User Profile</h1>
    </div>
  );
}
